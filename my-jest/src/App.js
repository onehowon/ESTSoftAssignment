import sample from './sample.js'

export default class App{
    $target = null
    dsahboard = null

    constructor($target){
        this.$target = $target

        this.dsahboard = new Sample($target)
    }
}