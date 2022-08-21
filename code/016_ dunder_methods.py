class User:
    def __init__(self, value='test') -> None:
        self.value = value
        
    def __len__(self) -> int:
        return len(self.value)

    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return f'<{self.value} object>'
    
    def __del__(self):
        print('Экземпляр класса был удален')
