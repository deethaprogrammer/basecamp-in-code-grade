class PasswordManager:
    def __init__(self):
        self.old_passwords = []
        pass
    
    def get_password(self):
        return self.old_passwords[-1] if self.old_passwords else None
    
    def set_password(self, password):
        if not self.is_correct(password):
            self.old_passwords.append(password)
    
    def is_correct(self, password):
        return password in self.old_passwords