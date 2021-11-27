let vm = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],
    data: {
        Posts: [],
        Users: {}
    },
    methods: {
        changeLike: async function (postId) {
            console.log(postId)
            let data = await api("changeLiked", { postId: postId });
            console.log(data)
            if (data.value) {
                let post = this.Posts.filter(post => post.id == postId)[0]
                post.isLiked = data.value.isliked;
                post.likesCount = data.value.likesCount
            }
        },
        changeDisLike: async function (postId) {
            let data = await api("changeDisLiked", { postId: postId });
            console.log(data)
            if (data.value) {
                let post = this.Posts.filter(post => post.id == postId)[0]
                post.isDisliked = data.value.isDisliked;
                post.disLikesCount = data.value.disLikesCount
            }
        }
    }
})
let lastPost = 0;
async function load() {
    let posts = (await api("getPosts", { offset: lastPost, count: 20 })).data;
    lastPost += posts.length;
    for (post of posts) {
        if (!vm.Users[post.userId])
            vm.Users[post.userId] = await api("getUser", { id: post.userId }); 
    }
    vm.Posts = [...vm.Posts,...posts];
}
$(window).scroll(async function(){
    if($(window).scrollTop()+$(window).height()>=$(document).height()){
        let count=await load();
    }
})
load().then();