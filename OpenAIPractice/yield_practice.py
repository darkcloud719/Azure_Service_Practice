def generate_squares(n):

    print("Start generating squares...")
    for i in range(n):
        print(f"Yielding {i} * {i} = {i * i}")
        yield i * i
    print("Done generating squares.")

squares = generate_squares(5)

for num in squares:
    print(f"Received: {num}")


    