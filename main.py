def buggy_function(param):
    # Intentional Code Smell: Unused local variable (SonarCloud sẽ flag ~2-5 debt minutes)
    unused_var = param.upper()  # Variable defined but never used
    unused_var2 = 42  # Another unused one for more issues
    
    # Intentional Bug: Potential division by zero (runtime error, high severity)
    if param == 0:
        result = 10 / param  # Division by zero!
    else:
        result = 10 / 0  # Always division by zero here
    
    # Intentional Bug: Type error (comparing incompatible types, SonarCloud's type inference detects)
    import platform
    if platform.architecture() == "32bit":  # Error: tuple == str (always False, never succeeds)
        print("32-bit system")
    else:
        print("64-bit system")  # This will always run
    
    print("Function executed with bugs!")

# Call the function to trigger
buggy_function("test")  # Pass string, but bugs are in logic
