import axios from 'axios'
const baseUrl = 'http://localhost:3002'

const sendCode = (language, code) => {
	console.log(language, code)
	const object = {'language': language, 'script':code}
	console.log(object)

	// const promise = axios.get(baseUrl)
	// return promise.then(promise => promise.data)

	const promise = axios.post(baseUrl+'/code_run', object)
	console.log(promise)
	return promise.then(promise => promise.data)
}

const getAvailableLanguages = () => {
	console.log(baseUrl+"/languages")

	const promise = axios.get(baseUrl+"/languages")
	// console.log(promise.data)
	return promise.then(promise => promise.data)
}

export default {
	sendCode,
	getAvailableLanguages
};