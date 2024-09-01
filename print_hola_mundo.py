import os

def main():
  nombre = os.getenv("USERNAME")
  print("Hola {nombre}")

if __name__ == "__main__":
  main()
