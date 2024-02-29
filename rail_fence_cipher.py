def rail_fence_encrypt(n, k, outputList=False):
    message = n
    rail_count, rep = k
    rail_fences = [len(message) * [None] for n in range(rail_count)]
    pattern = list(range(rail_count)) + list(range(rail_count - 2, 0, -1))
    for _ in range(rep):
        for index, char in enumerate(message):
            rail_fences[pattern[index % len(pattern)]][index] = char
        message = [char for rail_fence in rail_fences for char in rail_fence if char is not None]
    return message if outputList else ''.join(message)

def rail_fence_decrypt(n, k):
    message = n
    rail_count, rep = k
    input_pos = range(len(message))
    output_pos = rail_fence_encrypt(input_pos, (rail_count, rep), True)
    result = ''
    for n in input_pos:
        result += message[output_pos.index(n)]
    return result