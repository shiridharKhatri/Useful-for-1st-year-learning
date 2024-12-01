function modify_list(lst){
    lst.push(4)
    lst = [5, 6, 7]
    return lst
}

let my_list = [1, 2, 3]
let result = modify_list(my_list)
console.log(my_list)
console.log(result)
