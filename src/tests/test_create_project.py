

def test_create_project(driver, create_project, do_login):
    # Step 1 Create test project via API.
    project_name = create_project
    # Step 2 Login into mobile application.
    do_login(driver)
    # Step 3 Verify on mobile that project is created
