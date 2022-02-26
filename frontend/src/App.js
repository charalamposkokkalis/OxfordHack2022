import { useState, useEffect } from "react";
import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ArticleList from "./Components/ArticleList";
import Home from "./Components/Home";
import Drawer from "@mui/material/Drawer";
import Box from "@mui/material/Box";
import AppBar from "@mui/material/AppBar";
import Typography from "@mui/material/Typography";
import Toolbar from "@mui/material/Toolbar";
import Divider from "@mui/material/Divider";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";

function App() {
  // const [articles, setArticles] = useState([]);

  // Modify the current state by setting the new data to
  // the response from the backend
  /*
  useEffect(() => {
    fetch("http://localhost:5000/articles", {
      methods: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((response) => setArticles(response))
      .catch((error) => console.log(error));
  }, []);
*/

  return (
    <Box sx={{ display: "flex" }}>
      {/*
      <AppBar
        position="fixed"
        sx={{ width: `calc(100% - 240px)`, ml: `240px`, minHeight: 65 }}
      >
        <Typography> AppBar </Typography>
      </AppBar>
      */}
      <Drawer
        sx={{
          width: 240,
          flexShrink: 0,
          "& .MuiDrawer-paper": {
            width: 240,
            boxSizing: "border-box",
          },
        }}
        variant="permanent"
        anchor="left"
      >
        <Toolbar />
        <Divider />
        <List>
          {["Inbox", "Starred", "Send email", "Drafts"].map((text, index) => (
            <ListItem button key={text}>
              <ListItemText primary={text} />
            </ListItem>
          ))}
        </List>
      </Drawer>
      <BrowserRouter>
        <Routes>
          <Route exact path="/" element={<Home />} />
          {/*
          <div className="App container m-4">
          <div className="row">
            <div className="text-center">
            <h1>Connecting a React Frontend to a Flask Backend.</h1>
            </div>
          </div>

          <ArticleList 
            articles={articles} 
            />

          </div>
          */}
        </Routes>
      </BrowserRouter>
    </Box>
  );
}

export default App;
