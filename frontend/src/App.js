import { useState, useEffect } from "react";
import "./App.css";
import { BrowserRouter, Route, Routes, Link } from "react-router-dom";
import Home from "./Components/Home";
import Drawer from "@mui/material/Drawer";
import Box from "@mui/material/Box";
import AppBar from "@mui/material/AppBar";
import Typography from "@mui/material/Typography";
import Toolbar from "@mui/material/Toolbar";
import Divider from "@mui/material/Divider";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import Solutions from "./Components/Solutions";

function App() {
  return (
    <Box
      sx={{
        display: "flex",
        mt: 10,
        ml: 2,
        color: "green",
      }}
    >
      <AppBar
        position="fixed"
        sx={{
          width: `calc(100% - 240px)`,
          ml: `240px`,
          minHeight: 65,
          backgroundColor: "green",
        }}
      >
        <Typography sx={{ ml: "50%" }}> CarbonBlock </Typography>
      </AppBar>
      <Drawer
        sx={{
          width: 240,
          flexShrink: 0,
          "& .MuiDrawer-paper": {
            width: 240,
            boxSizing: "border-box",
            backgroundColor: "green",
            color: "white",
          },
        }}
        variant="permanent"
        anchor="left"
      >
        <Toolbar />
        <Divider />
        <List>
          <ListItem button key={"My Portfolio"}>
            <ListItemText primary={"My Portfolio"} />
          </ListItem>
          <ListItem button key={"Solutions"}>
            <ListItemText primary={"Solutions"} />
          </ListItem>
          <ListItem button key={"About Us"}>
            <ListItemText primary={"About Us"} />
          </ListItem>
        </List>
      </Drawer>
      <BrowserRouter>
        <Routes>
          <Route
            path="/solutions"
            element={<Solutions sols={["sol1", "sol2"]} />}
          />
          <Route path="/" element={<Home />} />
        </Routes>
      </BrowserRouter>
    </Box>
  );
}
export default App;
