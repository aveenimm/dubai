flat_number = int(input())
block_section = (flat_number - 1) // 20 + 1
floor_number = (flat_number - 1) % 20 // 4 + 1
print(block_section)
print(floor_number)