import argparse
import itertools
import json
import math
from fractions import Fraction


def determinant(matrix):
    rows = [[Fraction(entry) for entry in row] for row in matrix]
    result = Fraction(1)
    for column in range(len(rows)):
        pivot = next((index for index in range(column, len(rows))
                      if rows[index][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            rows[pivot], rows[column] = rows[column], rows[pivot]
            result = -result
        diagonal = rows[column][column]
        result *= diagonal
        for index in range(column + 1, len(rows)):
            factor = rows[index][column] / diagonal
            for position in range(column + 1, len(rows)):
                rows[index][position] -= factor * rows[column][position]
    return result


def stirling_tables(limit):
    first = [[0] * (limit + 1) for _ in range(limit + 1)]
    second = [[0] * (limit + 1) for _ in range(limit + 1)]
    first[0][0] = second[0][0] = 1
    for row in range(1, limit + 1):
        for column in range(1, row + 1):
            first[row][column] = (first[row - 1][column - 1]
                                   + (row - 1) * first[row - 1][column])
            second[row][column] = (second[row - 1][column - 1]
                                    + column * second[row - 1][column])
    return first, second


FIRST, SECOND = stirling_tables(40)


def stirling_minor(n_value, k_value, m_value):
    return determinant([[FIRST[n_value + m_value + row + 1][n_value + column + 1]
                         for column in range(k_value)] for row in range(k_value)])


def symmetric_values(alphabet, degree, complete):
    values = [Fraction(1)] + [Fraction(0)] * degree
    for node in alphabet:
        positions = range(1, degree + 1) if complete else range(degree, 0, -1)
        for position in positions:
            values[position] += node * values[position - 1]
    return values


def schur_rectangle(alphabet, k_value, m_value):
    values = symmetric_values(alphabet, k_value + m_value, True)
    return determinant([[values[k_value + row - column]
                         if k_value + row >= column else 0
                         for column in range(m_value)] for row in range(m_value)])


def alternant_rectangle(alphabet, k_value, m_value):
    size = len(alphabet)
    numerator = [[node ** (size - row - 1 + (k_value if row < m_value else 0))
                  for node in alphabet] for row in range(size)]
    denominator = [[node ** (size - row - 1) for node in alphabet]
                   for row in range(size)]
    return determinant(numerator) / determinant(denominator)


def nested_sum(n_value, m_value, exponent):
    total = Fraction(0)
    chain_count = 0
    normalization = math.prod(math.factorial(n_value + position)
                              for position in range(m_value))
    for increasing in itertools.combinations_with_replacement(range(n_value + 1), m_value):
        chain = tuple(reversed(increasing))
        chain_count += 1
        term = Fraction((-1) ** sum(chain))
        for earlier in range(m_value):
            for later in range(earlier + 1, m_value):
                term *= (chain[earlier] - chain[later] + later - earlier) ** 2
        for position, value in enumerate(chain):
            falling = math.factorial(n_value + position) // math.factorial(n_value + position - value)
            node = n_value - value + position + 1
            term *= Fraction(falling, math.factorial(value + m_value - position - 1))
            term *= Fraction(node) ** exponent
        total += term
    return total / normalization, chain_count


def subset_sum(alphabet, m_value, exponent):
    total = Fraction(0)
    for indices in itertools.combinations(range(len(alphabet)), m_value):
        selected = set(indices)
        numerator = math.prod(alphabet[index] ** exponent for index in indices)
        denominator = math.prod(alphabet[index] - alphabet[other]
                                for index in indices for other in range(len(alphabet))
                                if other not in selected)
        total += numerator / denominator
    return total


def integer_exponent_expected(alphabet, m_value, exponent):
    n_value = len(alphabet) - m_value
    if n_value == 0:
        return math.prod(alphabet) ** exponent
    if exponent >= n_value:
        return schur_rectangle(alphabet, exponent - n_value, m_value)
    if exponent > -m_value:
        return Fraction(0)
    width = -m_value - exponent
    return ((-1) ** (n_value * m_value) * math.prod(alphabet) ** exponent
            * schur_rectangle(alphabet, width, n_value))


def polynomial_product(left, right):
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for first_index, first_value in enumerate(left):
        for second_index, second_value in enumerate(right):
            result[first_index + second_index] += first_value * second_value
    return result


def extended_checks():
    counts = dict(integer_chain_cases=0, integer_chain_instances=0,
                  integer_alphabet_cases=0, zero_n_integer_cases=0,
                  rational_row_series_coefficients=0, companion_recurrence_pairs=0,
                  weighted_row_cases=0, weighted_homogeneous_cases=0,
                  corrected_egf_coefficients=0, corrected_riordan_coefficients=0)
    for n_value in range(6):
        for m_value in range(1, 5):
            alphabet = [Fraction(position) for position in range(1, n_value + m_value + 1)]
            for exponent in range(-m_value - 4, n_value + 5):
                actual, chain_count = nested_sum(n_value, m_value, exponent)
                expected = integer_exponent_expected(alphabet, m_value, exponent)
                assert actual == expected == subset_sum(alphabet, m_value, exponent)
                counts['integer_chain_cases'] += 1
                counts['integer_chain_instances'] += chain_count
                if n_value == 0:
                    counts['zero_n_integer_cases'] += 1
    for size in range(2, 7):
        alphabet = [Fraction((-1) ** position * (position * position + 1), position + 1)
                    for position in range(1, size + 1)]
        for m_value in range(1, size):
            for exponent in range(-m_value - 3, size - m_value + 4):
                assert (subset_sum(alphabet, m_value, exponent)
                        == integer_exponent_expected(alphabet, m_value, exponent))
                counts['integer_alphabet_cases'] += 1
    for n_value in range(5):
        for m_value in range(1, 4):
            alphabet = list(range(1, n_value + m_value + 1))
            factors = []
            weights = []
            for indices in itertools.combinations(alphabet, m_value):
                selected = set(indices)
                root = math.prod(indices)
                denominator = math.prod(node - other for node in indices for other in alphabet
                                        if other not in selected)
                factors.append([Fraction(1), Fraction(-root)])
                weights.append(Fraction(root ** n_value, denominator))
            denominator_poly = [Fraction(1)]
            for factor in factors:
                denominator_poly = polynomial_product(denominator_poly, factor)
            numerator_poly = [Fraction(0)] * len(denominator_poly)
            for omitted, weight in enumerate(weights):
                product_poly = [Fraction(1)]
                for index, factor in enumerate(factors):
                    if index != omitted:
                        product_poly = polynomial_product(product_poly, factor)
                for degree, coefficient in enumerate(product_poly):
                    numerator_poly[degree] += weight * coefficient
            coefficients = [schur_rectangle(alphabet, degree, m_value)
                            for degree in range(len(denominator_poly) + 4)]
            for degree in range(len(coefficients)):
                coefficient = sum(denominator_poly[index] * coefficients[degree - index]
                                  for index in range(min(degree, len(denominator_poly) - 1) + 1))
                assert coefficient == (numerator_poly[degree] if degree < len(numerator_poly) else 0)
                counts['rational_row_series_coefficients'] += 1
    for size in range(1, 16):
        harmonic = sum((Fraction(1, position) for position in range(1, size + 1)), Fraction(0))
        row = FIRST[size][:size + 1]
        assert sum(row) == math.factorial(size)
        assert sum(index * value for index, value in enumerate(row)) == math.factorial(size) * harmonic
        assert sum((index + 1) * value for index, value in enumerate(row)) == math.factorial(size) * (harmonic + 1)
        assert sum((index - 1) * value for index, value in enumerate(row)) == math.factorial(size) * (harmonic - 1)
        assert sum(index * row[size - index] for index in range(size + 1)) == math.factorial(size) * (size - harmonic)
        counts['weighted_row_cases'] += 1
        for first_variable in range(-2, 4):
            for second_variable in range(-2, 4):
                assert (sum(row[index] * first_variable ** index * second_variable ** (size - index)
                            for index in range(size + 1))
                        == math.prod(first_variable + position * second_variable for position in range(size)))
                counts['weighted_homogeneous_cases'] += 1
        for column in range(1, size):
            expected = (size - column) * FIRST[size][column]
            by_row = sum(math.comb(column + offset - 1, offset) * FIRST[size][column + offset - 1]
                         for offset in range(2, size - column + 2))
            by_column = sum(math.factorial(offset - 2) * math.comb(size, offset)
                            * FIRST[size - offset + 1][column]
                            for offset in range(2, size - column + 2))
            assert expected == by_row == by_column
            counts['companion_recurrence_pairs'] += 1
    maximum_degree = 14
    logarithm = [Fraction(0)] + [Fraction(1, index) for index in range(1, maximum_degree + 1)]
    power = [Fraction(1)]
    for column in range(maximum_degree + 1):
        for degree in range(maximum_degree + 1):
            actual = power[degree] / math.factorial(column) if degree < len(power) else Fraction(0)
            assert actual == Fraction(FIRST[degree][column], math.factorial(degree))
            counts['corrected_egf_coefficients'] += 1
            shifted = sum(power[:degree + 1]) / math.factorial(column)
            assert shifted == Fraction(FIRST[degree + 1][column + 1], math.factorial(degree))
            counts['corrected_riordan_coefficients'] += 1
        power = polynomial_product(power, logarithm)[:maximum_degree + 1]
    assert Fraction(FIRST[2][2], math.factorial(2)) == Fraction(1, 2)
    assert polynomial_product(logarithm, logarithm)[2] == 1
    assert FIRST[1][0] == 0 and FIRST[2][1] == 1
    printed_weight_sum = Fraction(1)
    corrected_weight_sum = Fraction(-1) + Fraction(2) * 2
    assert printed_weight_sum != corrected_weight_sum == stirling_minor(1, 1, 1) == 3
    assert SECOND[4][2] == 7 and schur_rectangle([1, 2, 3], 2, 1) == 25
    assert SECOND[4][2] == schur_rectangle([1, 2], 2, 1)
    return {'status': 'all identities agree', 'counts': counts,
            'ranges': {'integer_chains': '0 <= n <= 5; 1 <= m <= 4; -m-4 <= a <= n+4',
                       'integer_alphabets': '2 <= N <= 6; 1 <= m < N; -m-3 <= a <= N-m+3; x_i=(-1)^i(i^2+1)/(i+1)',
                       'row_series': '0 <= n <= 4; 1 <= m <= 3; coefficients through degree binomial(n+m,m)+4',
                       'companion_recurrences': '1 <= k < v <= 15',
                       'weighted_rows': '1 <= v <= 15; -2 <= b,x <= 3',
                       'column_egf': '0 <= v,k <= 14'}}


def run_checks():
    counts = dict(a396563_parameter_triples=0, a396563_chain_instances=0,
                  empty_sum_extension=0, reciprocal_parameter_pairs=0,
                  reciprocal_chain_instances=0, alphabet_identities=0,
                  a396563_displayed_cells=0)
    for n_value in range(7):
        for k_value in range(7):
            for m_value in range(1, 6):
                alphabet = list(range(1, n_value + m_value + 1))
                direct = stirling_minor(n_value, k_value, m_value)
                nested, chain_count = nested_sum(n_value, m_value, n_value + k_value)
                elementary = symmetric_values(alphabet, m_value + k_value, False)
                elementary_minor = determinant([[elementary[m_value + row - column]
                                                if m_value + row >= column else 0
                                                for column in range(k_value)]
                                               for row in range(k_value)])
                moment = (-1) ** (m_value * (m_value - 1) // 2) * determinant([
                    [SECOND[n_value + k_value + row + column + 1][n_value + m_value]
                     for column in range(m_value)] for row in range(m_value)])
                second_kind_minor = determinant([
                    [SECOND[n_value + k_value + row + 1][n_value + column + 1]
                     for column in range(m_value)] for row in range(m_value)])
                assert direct == nested == elementary_minor == moment == second_kind_minor
                assert direct == schur_rectangle(alphabet, k_value, m_value)
                assert direct == alternant_rectangle(alphabet, k_value, m_value)
                assert direct.denominator == 1 and direct >= math.factorial(m_value) ** k_value
                counts['a396563_parameter_triples'] += 1
                counts['a396563_chain_instances'] += chain_count
            assert stirling_minor(n_value, k_value, 0) == 1
            assert nested_sum(n_value, 0, n_value + k_value)[0] == 1
            counts['empty_sum_extension'] += 1
    for n_value in range(7):
        for m_value in range(1, 6):
            normalized, chain_count = nested_sum(n_value, m_value, -m_value - 1)
            size = n_value + m_value
            unnormalized = normalized * math.prod(math.factorial(n_value + position)
                                                   for position in range(m_value))
            prefactor = math.factorial(size) * math.prod((n_value + position) ** position
                                                        for position in range(1, m_value + 1))
            assert ((-1) ** (n_value * m_value) * prefactor * unnormalized
                    == FIRST[size + 1][m_value + 1])
            counts['reciprocal_parameter_pairs'] += 1
            counts['reciprocal_chain_instances'] += chain_count
    for size in range(1, 7):
        alphabet = [Fraction(position * position + 1, position + 1)
                    for position in range(1, size + 1)]
        for m_value in range(size + 1):
            for k_value in range(5):
                assert (subset_sum(alphabet, m_value, size - m_value + k_value)
                        == schur_rectangle(alphabet, k_value, m_value)
                        == alternant_rectangle(alphabet, k_value, m_value))
                counts['alphabet_identities'] += 1
    for n_value in range(7):
        for k_value in range(7):
            actual = stirling_minor(n_value, k_value, 2)
            if n_value == 0:
                assert actual == 2 ** k_value
            if n_value == 1:
                assert actual == 3 * 6 ** k_value - 3 * 3 ** k_value + 2 ** k_value
            if k_value == 0:
                assert actual == 1
            if k_value == 1:
                assert actual == Fraction((n_value + 1) * (n_value + 2) * (n_value + 3)
                                         * (3 * n_value + 8), 24)
    displayed = [
        [1, 2, 4, 8, 16, 32, 64],
        [1, 11, 85, 575, 3661, 22631, 137845],
        [1, 35, 725, 11935, 173901, 2360295, 30673525],
        [1, 85, 3850, 129360, 3665151, 93355395, 2216707900],
        [1, 175, 15190, 929334, 46149327, 2000578965, 79000290160],
        [1, 322, 48804, 5012406, 405247689, 27912905328, 1717078544896],
    ]
    for n_value, row in enumerate(displayed):
        for k_value, expected in enumerate(row):
            assert stirling_minor(n_value, k_value, 2) == expected
            counts['a396563_displayed_cells'] += 1
    return {'status': 'all identities agree', 'arithmetic': 'exact rational',
            'ranges': {'a396563': '0 <= n,k <= 6; 1 <= m <= 5',
                       'reciprocal': '0 <= n <= 6; 1 <= m <= 5',
                       'alphabets': 'N=1,...,6; x_i=(i^2+1)/(i+1); 0 <= m <= N; 0 <= k <= 4'},
            'counts': counts, 'integer_exponent_and_sibling_checks': extended_checks()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Exact checks of rectangular Schur and Stirling identities.')
    parser.parse_args()
    print(json.dumps(run_checks(), sort_keys=True, indent=2))
