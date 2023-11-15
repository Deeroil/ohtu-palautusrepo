*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

***Test Cases***
Register With Valid Username And Password
    Set Username  kallekalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is invalid

Register With Valid Username And Invalid Password
# # salasana ei sisällä halutunlaisia merkkejä
    Set Username  kaija
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Credentials
    Register Should Fail With Message  Password is invalid

Register With Nonmatching Password And Password Confirmation
    Set Username  kalleka
    Set Password  kalle123
    Set Password Confirmation  kalle456
    Submit Credentials
    Register Should Fail With Message  Password doesn't match confirmation

Register With Existing Username And Valid Password
    # Create User  kalle  kalle123
    Set Username  kallekalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  User with username kallekalle already exist

Login After Successful Registration
    Set Username  kissa
    Set Password  kissa123
    Set Password Confirmation  kissa123
    Submit Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  kissa
    Set Password  kissa123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is invalid
    Click Link  Login
    Set Username  k
    Set Password  kalle123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register
    