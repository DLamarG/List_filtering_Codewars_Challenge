function filter_list(l) {
    return l.filter(j=> typeof j != 'string')
   }


console.log(filter_list(['34', 2, 1, '76', 3]))
console.log(filter_list(['3', 2, 109, '6', 67]))
console.log(filter_list(['4', -90, 1, '-6', 600876]))
console.log(filter_list(['23454', 2, 14, '76', 27]))