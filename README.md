🏢📅 Room Booking System 🧑‍💻

This project is aimed at designing, building, and testing a room booking system. The main objective of the system is to avoid overlapping bookings and to let the booking manager know if a room is being booked, for how long, by whom, and when.

## Built With

- Firebase 🔥
  - Firestore for database
  - Firebase Auth for Google authentication
- Frontend
  - SvelteKit 🎉
    - Frontend framework
  - Typescript 📜
    - Type safety
  - Playwright 🎭
    - End-to-end testing
  - TailwindCSS 🎨
    - CSS framework of choice
    - quick and easy styling
- Backend
  - FastAPI 🚀
    - API endpoints & authorized routes
  - Pytest 🧪
    - Unit testing (Test Driven Development)
    - Test coverage
  - OpenAI GPT-3.5 🤖
    - Parsing natural language

## Requirements

- 🧪 Test Driven Development (TDD)

  - 🐞 Bug reporting
  - 🎯 Criteria-based test design

- 📝 Write good tests with a strategic rationale.
- 👨‍💻 Focus on testing during development.
- 🤝 Project Interview with Group: Present and defend what you've built and tested.

## Usage

### Prerequisites

- Node.js
- Python 3.11 or Higher
- An internet connection

### Setup

1. Backend

- in `/Backend` directory run:
  - start the web server
    - if on mac
    ```sh
    ./start.sh
    ```
    - if on windows
    ```bash
    ./start.bat
    ```

2. Frontend

- in `/Frontend` directory run:

  - the backend must be running for the frontend to function.

  ```sh
  cd frontend
  npm install
  npm run dev
  ```

## Testing

### Prerequisites

- Node.js
- Python 3.10 or Higher
- An internet connection
- Java 11 or higher (for Firebase emulator)

### Setup

#### Backend

Our framework of choice is pytest. however, we need to test our code that uses Firestore and Firebase auth. we were able to test these without needing to make API calls to the normal Firebase service by using [Firebase emulator](https://firebase.google.com/docs/emulator-suite) which creates a local instance of Firebase for testing purposes. in a way, it's just a very fancy mock library.

- in `/Backend` directory run:

  - install Firebase emulator
    ```sh
    npm install -g firebase-tools
    ```
  - then run `firebase init` and press enter. allow it to download the necessary files.

  - to start the emulator with some preset data, run:
    ```sh
    firebase emulators:exec --only auth,firestore --import=test-emulator-default
    ```
  - this will run the emulator which must run in the background.
  - in another terminal window, run:

  ```sh
  pip install poetry
  poetry install
  ```

#### Frontend

The SvelteKit app uses playwright to do end-to-end testing.

- in `/Frontend` directory run:
  - download playwright browser binaries
  ```sh
  npx playwright install
  ```

### Running Tests

#### Backend

- in `/Backend` directory run:
  - run tests
  ```sh
  poetry run pytest
  ```
  - run tests with coverage
  ```sh
  poetry run pytest --cov=app ./tests/
  ```

#### Frontend

- in `/Frontend` directory run:

  - run playwright tests

  ```sh
  npm run test
  ```

  - run unit test

  ```sh
  npm run test:unit
  ```
