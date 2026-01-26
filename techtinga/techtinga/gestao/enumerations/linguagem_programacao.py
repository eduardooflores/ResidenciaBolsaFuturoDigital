from django.db import models

class LinguagemProgramacao(models.TextChoices):
    PYTHON = "Python", "Python"
    JS = "JavaScript", "JavaScript"
    JAVA = "Java", "Java"
    CSHARP = "C#", "C#"
    CPLUS = "C++", "C++"
    C = "C", "C"
    PHP = "Php", "Php"
    DART = "Dart", "Dart"