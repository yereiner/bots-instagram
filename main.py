import instaloader
import sys
import time
import random
def follow_user_from_multiple_accounts_with_delay(username_to_follow, account_usernames, min_delay=5, max_delay=15):
    L = instaloader.Instaloader()

    for instagram_username in account_usernames:
        try:
            L.load_session_from_file(instagram_username)
            print(f"Sesión cargada exitosamente para {instagram_username}.")
        except FileNotFoundError:
            instagram_password = input(f"Ingrese la contraseña de Instagram para {instagram_username}: ")
            try:
                L.login(instagram_username, instagram_password)
                L.save_session_to_file()
                print(f"Inicio de sesión exitoso y sesión guardada para {instagram_username}.")
            except instaloader.exceptions.BadCredentialsException:
                print(f"Error: Credenciales incorrectas para {instagram_username}.")
                continue

        try:
            profile = instaloader.Profile.from_username(L.context, username_to_follow)
        except instaloader.exceptions.ProfileNotExistsException:
            print(f"Error: El usuario '{username_to_follow}' no existe.")
            continue

        try:
            L.context.do_follow(profile.userid)
            print(f"{instagram_username} ha seguido a {username_to_follow} exitosamente.")
        except Exception as e:
            print(f"Error al intentar seguir a {username_to_follow} desde {instagram_username}: {e}")

        delay = random.randint(min_delay, max_delay)
        print(f"Esperando {delay} segundos antes del próximo follow...")
        time.sleep(delay)
if __name__ == "__main__":
    user_to_follow = input("Ingrese el nombre de usuario de Instagram que desea seguir: ")
    account_usernames = input("Ingrese los nombres de usuario de las cuentas que seguirán (separados por comas): ").split(",")
    account_usernames = [username.strip() for username in account_usernames]
    follow_user_from_multiple_accounts_with_delay(user_to_follow, account_usernames)

