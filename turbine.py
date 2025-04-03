
def calculate_reactivity(l, d1, alpha1, alpha2, beta1, beta2, low_type):
    """Функция расчета степени реактивности ступени

    Args:
        l (_type_): высота лопатки
        d1 (_type_): средний диаметр
        alpha1 (_type_): альфа1
        alpha2 (_type_): альфа2
        beta1 (_type_): бетта1
        beta2 (_type_): бетта2
        low_type (_type_): тип закона (существуют разные формулы, чтобы можно было поразному считать)
    """
    if low_type == 1:
        rho = 89
    elif low_type == 2:
        rho = 90
    else:
        rho = 1
    return rho

if __name__ == '__main__':
    print(calculate_reactivity(1, 1, 1, 1, 1, 1, 2))
