function compareItems(item1, item2){
    result= {}
    const {phone, address, gender} = item1;
    const {phone: phone2, address: address2, gender: gender2} = item2;
    if(phone !== phone2){
        result.phone = phone
    }
    
    if(address !== address2){
        result.address = address
    }
    
    if(gender !== gender2){
        result.gender = gender
    }
    console.log(Object.values(result));
    return result
}

const item1 = {phone:"09012345678", address:"BG", gender:"Male"};
const item2 = {phone:"9", address:"BG", gender:"Male"};

// console.log(compareItems(item1,item2))


function getDateDifference(date1, date2) {
    const MS_PER_DAY = 1000 * 60 * 60 * 24*365;
    const utc1 = Date.UTC(
      date1.getFullYear(),
      date1.getMonth(),
    );
    const utc2 = Date.UTC(
      date2.getFullYear(),
      date2.getMonth(),
    );
    const dateDiff = Math.floor((utc2 - utc1) / MS_PER_DAY)
    return dateDiff;
}

const date1 = new Date('1968-01-01')
const date2 = new Date()
console.log(getDateDifference(date1, date2));