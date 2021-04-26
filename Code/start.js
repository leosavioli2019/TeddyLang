const express = require('express');
const app = express();

app.get('/', (req,res) => {
    res.send(`
        <form method="GET" action="/code">
            <input type="text"/>
            <input type="submit"/>
        </form>
    `)
})

app.get('/code:code', (req, res) => {
    try {
        eval(req.query.code)
    } catch (error) {
        res.send(`<p id="is_not_correct">${error}<p>`)
    }
})

app.get('/front:code', (req, res) => {
    res.send(`
        <script>
            const p = document.getElementById("is_not_correct")
            const code = ${req.query.code}
            try{
                eval(code)
            }catch(error){
                p.innerText = error 
            }
        </script>    
    `)
})  