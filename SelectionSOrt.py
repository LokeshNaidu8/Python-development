def selectionSort(seq):
    for i in range(len(seq)):
        m=min(seq[i:])
        m_index=seq.index(m)
        seq[i],seq[m_index]=seq[m_index],seq[i]
    return seq



print(selectionSort([6,1,3,0,4,5]))
