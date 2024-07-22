import React, { Component } from "react";
import Form from "./components/Form";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: {
        name: "",
      },
    };
  }


  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">Form App</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <Form />
          </div>
        </div>
      </main>
    );
  }
}

export default App;
