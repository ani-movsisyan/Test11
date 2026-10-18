from pages.login.login import Login


description = '''
======================================
Owner:     Ani Movsisyan
Created:   Oktober 16, 2026
Test Case: Add Login data
======================================
Steps:
------
1. Click on the  menu
2. Add login field
3. Add password field 
4. Click on the 'Login' button
======================================
Expected Result:
-----------------
1. The user should login
2. The Success message appears
======================================
'''


def test_login(driver_init):
    login = Login(driver_init)
    login.login_process()


