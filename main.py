import test_stairmaster as test_module

# quick and dirty test runner
tests = [(name, func) for name, func in vars(test_module).items() if name.startswith("test_")]

for name, func in tests:
    print(f"{name}... ", end="")
    func()
    print("passed.")

# If a test fails, it will raise an error
# So if we get here, then all tests passed
print("All tests passed.")
