(function(){
// settings for ajax - getting cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
} 

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function updateIdeaData(data){
    $current_funders.html(data.get_current_funders)
    $current_quantity.html(data.get_current_quantity)
    $current_progress.attr('style', 'width:'+data.get_current_progress+"%")
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
var CommentForm = React.createClass({
    getInitialState: function() {
        return {content:''};
    },
    handleContentChange: function(e) {
        if (this.isMounted()) {
            this.setState({content: e.target.value});
        }
    },
    handleSubmit: function(e) {
        e.preventDefault();
        var content = this.state.content.trim();
        this.props.onCommentSubmit({content: content});
        if (this.isMounted()) {
            this.setState({content: ''});
        }
    },
    render: function(){
        return (
            <div className="form-group">
                <form className="commentForm" onSubmit={this.handleSubmit}>
                    <textarea 
                        className="form-control"
                        placeholder="Comment" 
                        value={this.state.content}
                        onChange={this.handleContentChange}
                        required
                    />
                    <input
                        className="btn btn-primary"
                        type="submit"
                        value="Post" 
                    />
                </form>
            </div>
        );
    }
});


var Text  = React.createClass({
  render: function() {
    return (
        <div className="media-body">
            <h5 className="media-heading">
                {this.props.content}
            </h5>
            <p>
                {this.props.username}
            </p>
        </div>
    );
  }
});

var Photo = React.createClass({
  render: function() {
    var divStyle = {
        height: 64,
        width: 64,
        borderRadius: 50,
        backgroundSize: 'cover',
        backgroundImage: 'url(' + this.props.src + ')',
    };
    return (
        <div className="media-left media-middle" >
            <div className="media-object" style={divStyle} />
        </div>
    );
  }
});

var Comment = React.createClass({
  render: function() {
    return (
        <div className="media">
            <Photo src={this.props.src}/>
            <Text 
                username={this.props.username}
                content={this.props.content}
                created_at={this.props.created_at}
            />
        </div>
    );
  }
});

var CommentList = React.createClass({
    render: function(){
        var commentNodes = {};
        commentNodes = this.props.data.map(function(comment) {
            return (
                <Comment 
                    key={comment.id}
                    username={comment.username} 
                    src={comment.user_profileimage_url} 
                    created_at={comment.created_at}
                    content={comment.content}
                />
            );
        });
        return (
            <div className="commentList">
                {commentNodes}
            </div>
        );
    }
});

var CommentBox = React.createClass({
    loadCommentsFromServer: function(){
        $.ajax({
            url: this.props.url+"/",
            dataType: 'json',
            cache: false,
            success: function(data) {
                if (this.isMounted()) {
                    this.setState({data: data});
                }
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    handleCommentSubmit: function(comment){
        $.ajax({
            url: this.props.url+"/",
            dataType: 'json',
            type: 'POST',
            data: comment,
            success: function(data) {
                if (this.isMounted()) {
                    this.setState({data: data});
                }
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    getInitialState: function() {
        return {data: []};
    },
    componentDidMount: function() {
        this.loadCommentsFromServer();
        setInterval(this.loadCommentsFromServer, this.props.pollInterval);
    }, 
    render: function(){
        return (
            <div>
                <CommentList data={this.state.data} />
                <CommentForm onCommentSubmit={this.handleCommentSubmit}/>
            </div>
        );
    }
});

var idea_url = "/ideas/explore/"+$('#comment-box').data('idea-id')+"/comment"


    $(document).ready(function(){
    
        ReactDOM.render(
            <CommentBox url={idea_url} pollInterval={1000} />,
            document.getElementById('comment-box')
        );
    });

})()
