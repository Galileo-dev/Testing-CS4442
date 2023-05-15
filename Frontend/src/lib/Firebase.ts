import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { getAuth } from 'firebase/auth';

// Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
	apiKey: 'AIzaSyC3tpjB0C0m56eXOGoZWKSjat2eSRZ2Nwg',
	authDomain: 'cs4442-testing-project.firebaseapp.com',
	projectId: 'cs4442-testing-project',
	storageBucket: 'cs4442-testing-project.appspot.com',
	messagingSenderId: '1016294378603',
	appId: '1:1016294378603:web:2c5df3c3a0acbfe28ef52e',
	measurementId: 'G-Z5J3PBXN2W'
};

export const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
export const auth = getAuth(app);
