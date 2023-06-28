opt=0;
ocurrencias={}
while opt!=5:
    print("MENU DE OPCIONES")
    print("1- Contar ocurrencias en un texto");
    print("2- Saber si un numero es positivo, negativo o cero");
    print("3- Guardar numeros enteros");
    print("4- Sumar dígitos de un numero entero");
    print("5- Salir");
    print(f"-------------------------------------------------------------");
    opt=int(input("Ingrese su opción: "));
    if opt==1:
        frase=input("Ingrese su frase");
        print(f"Su frase es: {frase}");
        for letra in frase:
            if not letra.isalpha():
                continue
            letra = letra.lower()
            ocurrencias[letra] = ocurrencias.get(letra, 0) + 1;
        print(ocurrencias);
    elif opt==2:
        numsInt=[];
        while True:
            num=input("Ingrese numero o ingrese * para terminar");
            if num=="*":
                break;
            numsInt.append(int(num))
        for n in numsInt:
            if n>0:
                print(f"{n} Es positivo");
            elif n<0:
                print(f"{n} Es negativo")
            else:
                print(f"{n} Es igual a 0");
    elif opt==3:
        numeros=[];
        while True:
            numInt=int(input("Ingre numero o ingrese 0 para terminar: "));
            if numInt==0:
                break;
            else:
                numeros.append(numInt);
        suma=sum(numeros);
        promedio=suma/len(numeros);
        print(f"Suma: {suma}");
        print(f"Promedio: {promedio}");
    elif opt==4:
        num4=[];
        num=input("Ingrese numero: ");
        for i in num:
            num4.append(int(i));
        suma=sum(num4)
        print(f"Suma: {suma}");
    elif opt==5:
        print("FIN DE PROGRAMA")
        print("=================================");
        break;
    else:
        print("Opción inválida. Intente nuevamente");
