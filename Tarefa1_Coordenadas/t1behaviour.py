import sys
print("Coordenada x do retangulo vai de -200 a 200.")
print("Coordenada y do retangulo vai de -100 a 100.")
print("Defina as coordedanas x e y do ponto")
x = input("Coordenada x: ")
y = input("Coordenada y: ")
ponto_escolhido = (int(x), int(y))
print(ponto_escolhido)

if (int(x) > 200 or int(x) < -200 or int(y) < -100 or int(y) > 100):{
    print("Coordenada fora da dimensao pre-estabelecida.")    
}
else:
    if(int(x) > 0 and int(y) > 0):
        print("O ponto escolhido esta para a direita e para cima com relacao a origem em (0,0).")
    elif(int(x) > 0 and int(y) < 0):
        print("O ponto escolhido esta para a direta e para baixo com relacao a origem em (0,0).")
    if(int(x) < 0 and int(y) > 0):
        print("O ponto escolhido esta para a esquerda e para cima com relacao a origem em (0,0).")
    elif(int(x) < 0 and int(y) > 0):
        print("O ponto escolhido esta para a esquerda e para baixo com relacao a origem em (0,0).")
    if(int(x) > 0 and int(y) == 0):
        print("O ponto esta para a direita em relacao a origem em (0,0)")
    elif(int(x) < 0 and int(y) == 0):
        print("O ponto esta para a esquerda em relacao a origem em (0,0)")
    if(int(x) == 0 and int(y) > 0):
        print("O ponto esta para cima em relacao a origem em (0,0)")
    elif(int(x) == 0 and int(y) < 0):
        print("O ponto esta para baixo em relacao a origem em (0,0)")
    if(int(x) == 0 and int(y) == 0):
        print("O ponto esta na origem.")
sys.exit()   








    

