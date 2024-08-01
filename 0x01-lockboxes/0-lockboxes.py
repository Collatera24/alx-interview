#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def look_next_opened_box(opened_boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the opened box
    """

    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    
    if len(boxes) == 0:
        return False

    if len(boxes) == 1 or boxes == [[]]:
        return True

    aux = {0: {'status': 'opened', 'keys': boxes[0]}}
    keys = look_next_opened_box(aux)


    while keys is not None:
        for key in keys:
            if key < len(boxes) and key not in aux:
                aux[key] = {'status': 'opened', 'keys': boxes[key]}
        keys = look_next_opened_box(aux)

    return len(aux) == len(boxes)

if __name__ == '__main__':
    def main():
        """Entry point"""
        canUnlockAll([[]])


    main()
