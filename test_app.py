from app import suma

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    #print("funcion terminada")


#test_suma()

def test_resta():
    assert resta(5, 2) == 3