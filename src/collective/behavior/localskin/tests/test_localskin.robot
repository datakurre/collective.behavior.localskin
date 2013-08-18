*** Settings ***

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot
Resource  plone/app/robotframework/saucelabs.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open SauceLabs test browser
Test Teardown  Run keywords  Report test status  Close all browsers

*** Test cases ***

Plone is up
    Enable autologin as  Member  Editor
    Set autologin username  test-user-
    Go to  ${PLONE_URL}
    Page should contain element  content-core
