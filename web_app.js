const express = require('express');
const app = express();
const engine =require('express-handlebars');
const path = require('path');
const route=require('./src/Route/index.route');
var exphbs  = require('express-handlebars');
var session=require('express-session');
 
var hbs = exphbs.create({
    // Specify helpers which are only registered on this instance.
    helpers: {
        foo: function () { return 'FOO!'; },
        bar: function () { return 'BAR!'; },
        // đắng ký thẻ <head>
        section: function (name, options) {
            if (!this._sections) this._sections = {};
            this._sections[name] = options.fn(this);
            return null;
        }
    }
    
});
//template handlebars
app.engine('handlebars', hbs.engine);
app.set('view engine', 'handlebars');
const bodyParser = require('body-parser');
app.set('views', path.join(__dirname,'src/View'));


app.use(session({
    secret: 'abcdefg',
    resave: true,
    saveUninitialized: true,
    cookie: { maxAge: 60000 }
  }));
// Sử dụng middleware body-parser
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());


const port=3000;
app.use(express.static(path.join(__dirname, 'code')));
///add router
route(app);

app.listen(port);
console.log(`Running at Port ${port}`);