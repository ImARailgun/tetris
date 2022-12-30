block_types = {
    "square": {
        "color": (255, 255, 0),
        "instructions": {
            "Two": [0, 1],
            "Three": [1, 0],
            "Four": [1, 1]
        },
        "rot_index": 5
    },
    "line": {
        "color": (0, 255, 255),
        "instructions": {
            "Two": [0, 1],
            "Three": [0, 2],
            "Four": [0, 3]
        },
        "rot_index": 0
    },

    "hook": {
        "color": (255, 128, 0),
        "instructions": {
            "Two": [0, 1],
            "Three": [0, 2],
            "Four": [1, 2]
        },
        "rot_index": 0
    },
    "hook-reverse": {
        "color": (0, 0, 204),
        "instructions": {
            "Two": [0, 1],
            "Three": [0, 2],
            "Four": [-1, 2]
        },
        "rot_index": 0
    },
    "T": {
        "color": (178, 102, 255),
        "instructions": {
            "Two": [1, 0],
            "Three": [1, 1],
            "Four": [2, 0]
        },
        "rot_index": 1
    },
    "zigzag": {
        "color": (255, 51, 51),
        "instructions": {
            "Two": [1, 0],
            "Three": [1, 1],
            "Four": [2, 1]
        },
        "rot_index": 2
    },
    "zigzag-reverse": {
        "color": (0, 204, 0),
        "instructions": {
            "Two": [0, 1],
            "Three": [1, 1],
            "Four": [1, 2]
        },
        "rot_index": 2
    },

}
