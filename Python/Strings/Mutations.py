def mutate_string(string, position, character):
    st=string[:position]+character+string[position+1:]
    return st

