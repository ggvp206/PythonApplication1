from browser import window, document, html

def setup_git():
  """����������� Git, ������� ����������� � ��������� .gitignore."""

  # ��������� ����� ������������ � �����
  # � Skulpt ��� ������� � �������� �������, �������
  # �� ��������� ��� ������ � ������� JavaScript.
  user_name = "���� ���"
  user_email = "����_�����@email.com"

  # �������� �����������
  repo_name = "my_project"

  # �������� ��������� HTML ��� ������������� �����
  # (�� �������� ��������� �������� ��������)
  repo_folder = html.DIV(repo_name)
  document.body <= repo_folder

  # �������� README.md
  readme_file = html.DIV(Class='readme', Text="# project3")
  repo_folder <= readme_file

  # ������������� �����������
  # � Skulpt ��� ������� ������� git init
  # �� ������ ������������ JavaScript ��� ������������ ���������
  # � ��������� ��������� HTML

  # �������� �������
  # � Skulpt ��� ������� ������� git status
  # �� ������ ������������ JavaScript ��� �������� ���������
  # � ��������� ��������� HTML

  # ���������� .gitignore
  # � Skulpt ��� ������� ������� wget
  # �� ������ ������������ JavaScript ��� �������� ������ � �������
  # � ���������� �� � ������� HTML

  # ���������� .gitignore � ������
  # � Skulpt ��� ������� ������� git add
  # �� ������ ������������ JavaScript ��� ������������ ���������
  # � ��������� ��������� HTML

  # �������� ������� �������
  # � Skulpt ��� ������� ������� git commit
  # �� ������ ������������ JavaScript ��� ���������� ������� 
  # ��������� � ���� ������� JavaScript

  # �������������� ����� � main
  # � Skulpt ��� ������� ������� git branch
  # �� ������ ������������ JavaScript ��� ���������� ����������
  # �������� ��������� HTML

  # ���������� ���������� �����������
  # � Skulpt ��� ������� ������� git remote
  # �� ������ ������������ JavaScript ��� �������� ������
  # �� ������ � ������� AJAX-��������

  # �������� ��������� �� GitHub
  # � Skulpt ��� ������� ������� git push
  # �� ������ ������������ JavaScript ��� �������� ������
  # �� ������ � ������� AJAX-��������

  # ����� � ����������� �������
  # � Skulpt ��� ������� ������� git log
  # �� ������ ������������ JavaScript ��� ��������� �������
  # ���������, �������� � ������� JavaScript

  # ����� � ����������� �������
  # � Skulpt ��� ������� ������� git reset
  # �� ������ ������������ JavaScript ��� �������������� 
  # ���������� ������ ��������� HTML

  print("Git ��������, ����������� ������!")

if __name__ == "__main__":
  setup_git()