input = """CAPITAL: SE W NW NE NW NE
DIRECTORS: S S W W S W NW W
MANAGER: N SE NW SW W W
FRANCHISE: E E NE SE S SE N E
LIMITED: W NE SW SE E N
COMMODITY: S E SE N SW W S SE
TAKEOVER: NW NE NE NW NE SE W
TRADEMARK: S NW W SE SW SE W SE"""

for line in input.split('\n'):
    local_nums = []
    for num in line.split(': ')[1].split(' '):
        if num == 'N':
            local_nums.append('1')
        elif num == 'NE':
            local_nums.append('1')
        elif num == 'E':
            local_nums.append('0')
        elif num == 'SE':
            local_nums.append('1')
        elif num == 'S':
            local_nums.append('0')
        elif num == 'SW':
            local_nums.append('0')
        elif num == 'W':
            local_nums.append('1')
        elif num == 'NW':
            local_nums.append('0')

    print(f"{line.split(': ')[0]}: {''.join(local_nums)}")