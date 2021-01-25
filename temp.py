
def txt2yaml():
    out = ''
    d = {}

    with open('members.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

        for line in lines:
            parts = line.split(':')
            d[parts[0].strip()] = [parts[1].strip()]


    import yaml



    with open('members.yaml', 'w', encoding='utf-8') as f:
        output = yaml.dump(d, Dumper=yaml.Dumper)
        f.write(output)
