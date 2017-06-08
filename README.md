# An Unofficial Wealthsimple API

I was working on a personal project and wanted to be able to see my current Wealthsimple AUM. Unfortunately there isn't an official API to grab this data so I figured that I might as well try my own hand at it. By the end I had made a pretty "interesting" REST API.

### How I did it:
- At first I tried regular webscraping with beautiful soup. It worked...until I realized that the site is rendered with JS. Good choice on them but oh boy did it make my job difficult 👍
- After that, I started using Selenium to actually open an instance of chrome and wait for the JS to render the DOM elements
- I found identifiers for each element that I needed to interact with (ie. css classes, form names etc.). Using the identifiers, I was able to enter data and click buttons that I needed to
- I then parsed and fetched my current AUM
- After that, I built the scraper into a REST API and deployed it on AWS

### Using the API
Submit a JSON to the server at (still working on getting a nice url)   
Here's what it should look like
```
{
  "email" : YOUR_EMAIL,
  "password" : YOUR_PASSWORD,
  "attempts" : NO_OF_ATTEMPTS  // The integer number of log-in attempts you want the scraper to do before it throws an error (I recommend 5)
}
```

You will receive a JSON back. Depending on how it goes and how many attempts you posted for, it can take anywhere from 10-40 seconds (actually loading the page takes so long). On average, it takes me about 15 seconds to receive a response.

If successful, the server will respond with:
```
{
  "Portfolio Value" : AUM // float to two decimals
}
```

If unsuccessful, the server will respond with and throw an error code of 500:
```
{
  "error" : "error. Servers Unresponsive. Check your log in info"
}
```

*P.S This is pretty much just for my own use and I totally get it if using some random person's API is sketchy
