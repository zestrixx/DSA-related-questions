let d = [{ 'name': 'mayank', 'age': 25 }, { 'name': 'singh', 'age': 20 }]

let val = d.filter(rec => {
    return rec.name.startsWith('m')
})

console.log(val)