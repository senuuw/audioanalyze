import pickle


def count_terms(pickle_path):

    with open(pickle_path, 'rb') as file:
        transcript = pickle.load(file)

    complete_text = ""
    for segment in transcript:
        complete_text += segment['text']

    clean_text = complete_text.replace("-", " ").lower()



    troop_cards = {
        "Archer Queen" : ["Queen"],
        "Archers" : [],
        "Baby Dragon" : ["Baby D"],
        "Balloon" : [],
        "Bandit" : [],
        "Bats" : [],
        "Battle Healer" : ["Healer"],
        "Battle Ram" : ["Ram"],
        "Berserker" : ["Berserky"],
        "Bomber" : [],
        "Boss Bandit" : [],
        "Bowler" : [],
        "Cannon Cart" : ["Cart"],
        "Dark Prince" : [],
        "Dart Goblin" : [],
        "Electro Dragon" : ["E Dragon", "E Drag"],
        "Electro Giant" : ["E Giant"],
        "Electro Spirit" : ["E Spirit"],
        "Electro Wizard" : ["E Wizard"],
        "Elite Barbarians" : ["E Barbs"],
        "Elixir Golem" : ["E Golem"],
        "Executioner" : [],
        "Fire Spirit" : [],
        "Firecracker" : [],
        "Fisherman" : [],
        "Flying Machine" : [],
        "Furnace" : [],
        "Giant Skeleton" : [],
        "Goblin Gang" : [],
        "Goblin Giant" : [],
        "Golden Knight" : [],
        "Guards" : [],
        "Heal Spirit" : [],
        "Hunter" : [],
        "Ice Golem" : [],
        "Ice Spirit" : [],
        "Ice Wizard" : [],
        "Lava Hound" : [],
        "Little Prince" : [],
        "Lumberjack" : [],
        "Magic Archer" : [],
        "Mega Knight" : [],
        "Mega Minion" : [],
        "Might Miner" : [],
        "Mini Pekka" : ["Mini P.E.K.K.A.", "mini schmecker"],
        "Minion Horde" : [],
        "Minions" : [],
        "Monk" : [],
        "Mother Witch" : [],
        "Musketeer" : [],
        "Night Witch" : [],
        "Pheonix" : [],
        "Princess" : [],
        "Ram Rider" : [],
        "Royal Ghost" : ["Ghost"],
        "Royal Giant" : [],
        "Royal Hogs" : ["Hogs"],
        "Royal Recruits" : ["Recruits"], 
        "Rune Giant" : [],
        "Skeleton Army" : ["Skarmy"],
        "Skeleton Barrel" : [],
        "Skeleton Dragons" : [],
        "Skeleton King" : [],
        "Skeletons" : ["Skellies", "smeletons"],
        "Sparky" : [],
        "Spear Goblins": [],
        "Spirit Empress" : [],
        "Suspicious Bush" : ["Bush"],
        "Three Musketeers" : [],
        "Valkyrie" : ["Valk"],
        "Wall Breaker" : [],
        "Zappies" : []
    }

    core_units = {
        "Barbarians" : [],
        "Giant" : [],
        "Goblins" : [],
        "Golem" : [], 
        "Knight" : [],
        "Miner" : [],
        "Witch" : [],
        "Pekka" : ["P.E.K.K.A."],
        "Prince" : [],
        "Witch" : [],
        "Wizard" : [],
    }

    spell_cards = {
        "Arrows": ["Arrow"],
        "Barbarian Barrel" : ["Barb Barrel"],
        "Clone" : [],
        "Earthquake" : [],
        "Fireball" : [],
        "Freeze" : [],
        "Giant Snowball" : ["Snowball"],
        "Goblin Barrel" : [],
        "Goblin Curse": ["Curse"],
        "Graveyard" : [],
        "Lightning" : [],
        "Mirror" : [],
        "Poison": [],
        "Rage": [],
        "Rocket" : [],
        "Royal Delivery": ["Delivery"],
        "Log": [],
        "Tornado" : [],
        "Vines" : ["Vine"],
        "Void" : [],
        "Zap" : []
    }

    building_cards = {
        "Barbarian Hut" : ["Barb Hut"],
        "Bomb Tower" : [],
        "Cannon" : [],
        "Elixir Collector": ["Pump"],
        "Goblin Cage": ["Cage"],
        "Goblin Drill" : ["Drill"],
        "Goblin Hut" : [],
        "Inferno Tower" : [],
        "Mortar" : [],
        "Tesla" : [],
        "X Bow" : ["Expo"],
        "Tombstone" : []
    }

    extra_words = {
        "Elixir" : [],
        "Bridge" : [],
        "Broken" : [],
        "Cycle" : ["Cycling"],
        "Damage" : [],
        "Chip" : [],
        "Left" : [],
        "Right" : [],
        "Evo" : ["Evolved"],
        "Defend" : ["Defending"],
        "Kill" : [],
        "Value" : []
    }

    search_dicts = [troop_cards, spell_cards, building_cards, core_units, extra_words]

    count_map = {

    }

    for search_dictionary in search_dicts:
        for search_term in search_dictionary:
            
            search_list = search_dictionary[search_term]
            search_list.insert(0, search_term)
            
            count = 0 
            for term in search_list:
                count += clean_text.count(term.lower())
                clean_text.replace(term.lower(), "")
            
            count_map[search_term] = count

    return count_map