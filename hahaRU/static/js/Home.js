let vm = new Vue({
    el: "#app",
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
                post.dislikesCount = data.value.dislikesCount
            }
        }
    }
})
let lastPost = 0;
async function load() {
    let posts = await api("getPosts", { Offset: lastPost, Count: 20 });
    lastPost += posts.length;
    for (Post of posts) {
        if (!vm.Users[Post.userId])
            vm.Users[Post.userId] = JSON.parse(await api("getUser", { id: Post.userId })); 
    }
    vm.Posts = [...vm.Posts,...posts];
}
$(window).scroll(async function(){
    if($(window).scrollTop()+$(window).height()>=$(document).height()){
        let count=await load();
    }
})
load().then();