*** Settings ***
Resource  resource.robot
Test Setup  Input New Command


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123 
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123 
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists
    

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Username is too short: less than 3 characters

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  kalle1  kalle123
    Output Should Contain  Username is invalid: not using only a-z

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle1
    Output Should Contain  Password too short: less than 8 chars

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password invalid: should not contain only a-z
