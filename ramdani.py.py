#Nama : RAMDANI HURDI
#Nim  : TI17200040

q = "y"
b = ""
while( q == "y"):
    def binary_tree(x):
        return [x, [], []]
    def insert_left(root, new_branch):
        t = root.pop(1)
        if len(t) > 1:
            root.insert(1, [new_branch, t, []])
        else:
            root.insert(1, [new_branch, [], []])
        return root
    def insert_right(root, new_branch):
        t = root.pop(2)
        if len(t) >1:
            root.insert(2, [new_branch, [], t])
        else:
            root.insert(2, [new_branch, [], []])
        return root
    def get_root_val(root): 
        return root[0]
    def set_root_val(root, new_val):
        root[0] = new_val
    def get_left_child(root):
        return root[1]
    def get_right_child(root):
        return root[2]  

    b = str(input("masukkan cuaca :"))
    x = binary_tree(b)
    insert_left(x, str(input("akar pohon :")))
    insert_left(x, str(input("pohon :")))
    insert_right(x, str(input("cabang kiri :")))
    insert_right(x, str(input("cabang kanan :")))
    l = get_left_child(x)
    #set_root_val(x, str(input("hasil :")))
    print(x)
    if (b == "hujan") or (b == "angin"):
        print("hasil : tidak bisa main")
    elif (b == "panas") or (b == "lembab"):
        print("hasil : boleh main") 

    q = input("mau ulang Y/N ")
