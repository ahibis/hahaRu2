let vm = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],
    data: {
        Posts: []
    },
    methods: {
        changeLike: async function (postId) {
            console.log(postId)
            let data = await api("changeContentLiked", { postId: postId, type: "video"  });
            console.log(data)
            if (data.value) {
                let post = this.Posts.filter(post => post.id == postId)[0]
                post.isLiked = data.value.isliked;
                post.likesCount = data.value.likesCount
            }
        },
        changeDisLike: async function (postId) {
            let data = (await api("changeContentDisLiked", { postId: postId, type:"video" })).data;
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
    let posts = await api("getContents", { Offset: lastPost, Count: 5, type:"video"  });
    lastPost += posts.length;
    vm.Posts = posts;
}
/*
$(window).scroll(async function(){
    if($(window).scrollTop()+$(window).height()>=$(document).height()){
        let count=await load();
    }
})*/
load().then();