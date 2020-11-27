def knightTour(n, path, u, limit):
    # n是层次，path是路径，u是当前路径，limit搜索总深度
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n + 1, path, nbrList[i], limit)
            i = i + 1
        if not done:  # 回溯
            path.pop()
            u.setColor('white')

    else:
        done = True
    return done
