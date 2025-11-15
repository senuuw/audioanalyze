import pickle
import heapq
import os

def count_terms(pickle_path):

    with open(pickle_path, 'rb') as file:
        transcript = pickle.load(file)

    complete_text = " ".join(seg["text"] for seg in transcript)

    clean_text = complete_text.replace("-", " ").replace(".", "")
    clean_text = clean_text.lower()
    
    troop_cards = {
        "Archer Queen" : ["Queen"],
        "Archers" : [],
        "Baby Dragon" : ["Baby D"],
        "Balloon" : [],
        "Bats" : [],
        "Battle Healer" : ["Healer"],
        "Battle Ram" : ["Ram"],
        "Berserker" : ["Berserky"],
        "Bomber" : [],
        "Boss Bandit" : [],
        "Bowler" : [],
        "Cannon Cart" : ["Cart"],
        "Dark Prince" : [],
        "Dart Goblin" : ["Dart", "Dark Goblin"],
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
        "Hog Rider" : ["Hog"],
        "Ice Golem" : [],
        "Ice Spirit" : [],
        "Ice Wizard" : ["Ice Wiz"],
        "Inferno Dragon" : [],
        "Lava Hound" : [],
        "Little Prince" : [],
        "Lumberjack" : [],
        "Magic Archer" : [],
        "Mega Knight" : [],
        "Mega Minion" : [],
        "Might Miner" : [],
        "Mini Pekka" : ["mini schmecker"],
        "Minion Horde" : [],
        "Minions" : [],
        "Monk" : [],
        "Mother Witch" : [],
        "Musketeer" : [],
        "Night Witch" : [],
        "Pheonix" : [],
        "Princess" : [],
        "Ram Rider" : [],
        "Rascals" : [],
        "Royal Ghost" : ["Ghost"],
        "Royal Giant" : [],
        "Royal Hogs" : ["Hogs"],
        "Royal Recruits" : ["Recruits"], 
        "Rune Giant" : [],
        "Skeleton Army" : ["Skarmy"],
        "Skeleton Barrel" : ["Skelly Barrel"],
        "Skeleton Dragons" : [],
        "Skeleton King" : [],
        "Skeletons" : ["Skellies", "Smeletons"],
        "Sparky" : [],
        "Spear Goblins": [],
        "Spirit Empress" : [],
        "Suspicious Bush" : ["Bush"],
        "Three Musketeers" : [],
        "Valkyrie" : ["Valk"],
        "Wall Breaker" : [],
        "Zappies" : [],
        "Electro Dragon" : ["E Dragon", "E Drag"],
        "Electro Giant" : ["E Giant"],
        "Electro Spirit" : ["E Spirit"],
        "Electro Wizard" : ["E Wizard", "E Wiz"],
        "Elite Barbarians" : ["E Barbs"],
        "Elixir Golem" : ["E Golem"]
    }

    core_units = {
        "Barbarians" : [],
        "Bandit" : [],
        "Giant" : [],
        "Goblins" : [],
        "Golem" : [], 
        "Knight" : [],
        "Miner" : [],
        "Witch" : [],
        "Pekka" : [],
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
        "Evo" : ["Evolved"],
        "Defend" : ["Defending"],
        "Kill" : [],
        "Value" : [],
        "Card" : [],
        "Bait" : [],
        "Push" : [],
        "Snipe" : [],
        "Tower" : [],
        "Unit" : [],
        "Back" : [],
        "Spam" : [],
        "Lane" : [],
        "Connect" : [],
        "Strategy" : [],
        "Spell" : []
    }

    search_dicts = [troop_cards, spell_cards, building_cards, core_units, extra_words]

    card_map = {}
    extra_map = {}

    for search_dictionary in search_dicts:
        for search_term in search_dictionary:
            
            search_list = search_dictionary[search_term]
            search_list.insert(0, search_term)
            
            count = 0 
            for term in search_list:
                count += clean_text.count(term.lower())
                clean_text = clean_text.replace(term.lower(), "")
            
            if search_dictionary != extra_words:
                card_map[search_term] = count
            else:
                extra_map[search_term] = count


    return clean_text, card_map, extra_map

if __name__ == "__main__":
    pickle_path = "transcripts\ fvOyAAjVJEk.pkl"
    clean_text, card_map, extra_map = count_terms(pickle_path)
    print("hello")