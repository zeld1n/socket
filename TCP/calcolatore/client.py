import socket

HOST = '127.0.0.1'  
PORTA = 65432       
DIMENSIONE_BUFFER = 1024

while True: 
    try:
        primo_numero = float(input("Inserisci il primo numero: "))
        operazione = input("Inserisci l'operazione (+, -, *, /): ")
        secondo_numero = float(input("Inserisci il secondo numero: "))

        messaggio = f"{primo_numero} {operazione} {secondo_numero}"

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_servizio:
            sock_servizio.connect((HOST, PORTA))
            print(f"Connesso al server {HOST}:{PORTA}")

            sock_servizio.sendall(messaggio.encode('utf-8'))
            print(f"Inviato al server: '{messaggio}'")

            dati = sock_servizio.recv(DIMENSIONE_BUFFER)

            print('Risultato ricevuto:', dati.decode('utf-8'))


    except ValueError:
        print("Input non valido.")
    except ConnectionRefusedError:
        print(f"Errore: Connessione rifiutata.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

    altra_operazione = input("\nVuoi fare un'altra operazione? (sì/no): ")
    if altra_operazione != 'sì' and altra_operazione != 'si':
        break
print("Client chiuso.")