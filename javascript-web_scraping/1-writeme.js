#!/usr/bin/node
const fs = require('fs')
const writeFile =(path, text)=>{

    try{
        content = fs.writeFileSync(path, text, 'utf-8')

    }

    catch (error){
        console.log(`${error}`)
    }

}

if (require.main === module){

    if (process.argv.length !== 4){
        console.log(`You provide ${process.argv.length - 2} args out of 2, please provide all args`)
    }

    else{
        const path = process.argv[2]
        const text = process.argv[3]

        writeFile(path, text)
    }
}
