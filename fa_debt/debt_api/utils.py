def modify_data(deduction, amount, voc: dict, key: str, rate=0.25):

    """ Изменяет состояние счёта при условии

    :param deduction: сумма на удержание со счёта
    :param amount: сумма на счету к моменту списания
    :param voc: информация
    :param key: вид информации
    :param rate: ставка
    
    """
    if deduction <= rate*amount:
        voc[key] = str(amount - deduction)
        return voc
    else:
        return
